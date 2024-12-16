def update_context(context, user_query):
    # Update the context with the new query
    context["history"] = context.get("history", []) + [user_query]
    return context
